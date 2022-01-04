#pragma once
#include<set>
#include<string>
#include<iostream>


using namespace std;

class Catalog
{
	Catalog(const string& name);
private:
	string name;
	set<shared_ptr<File>> files = {};
	set<shared_ptr<Catalog>> catalogs = {};
protected:
	void addFile(shared_ptr<File> new_file);
	void addCatalog(shared_ptr<Catalog> new_catalog);
	void deleteFile(shared_ptr<File> file);
	void deleteCatalog(shared_ptr<Catalog> catalog);
	set<shared_ptr<File>> getFiles() const;
	set<shared_ptr<Catalog>> getCatalogs() const;
	friend class Administrator;
	friend class Buffer;
	friend class Illustrator;
	friend class Secretary;
};

class Actor
{
public:
	Actor(const string& n, shared_ptr<Buffer> buf);
protected:
	string name;
	shared_ptr<Buffer> buffer;
};

class Secretary: public Actor
{
public:
	Secretary(const string& n, shared_ptr<Buffer> buf);
	void AddFileToCatalog(shared_ptr<File> file, shared_ptr<Catalog> catalog);
	shared_ptr<Document> FindDocument(const string& author, shared_ptr<Catalog> catalog);
	shared_ptr<Document> FindDocument(const string& heading, shared_ptr<Catalog> catalog);
};

class Writer: public Actor
{
public:
	Writer(const string& n, shared_ptr<Buffer> buf);
	void CreateDocument(const string& head, const string& text);
	void UpdateDocumentHeading(const string& head, shared_ptr<Document> doc);
	void UpdateDocumentText(const string& text, shared_ptr<Document> doc);
	void LinkIllustration(shared_ptr<Document> doc, shared_ptr<Illustration> ill);
	void UnlinkIllustration(shared_ptr<Document> doc, shared_ptr<Illustration> ill);
};

class Illustrator : public Actor
{
public:
	Illustrator(const string& n, shared_ptr<Buffer> buf);
	void CreateIllustration(const string& head);
	void AddIllustrationToCatalog(shared_ptr<Illustration> ill, shared_ptr<Catalog> catalog);
	void DeleteIllustration(shared_ptr<Illustration> ill, shared_ptr<Catalog> catalog);
	void DeleteIllustration(shared_ptr<Illustration> ill);
};

class Administrator : public Actor
{
public:
	Administrator(const string& n, shared_ptr<Buffer> buf);
	void CreateCatalog(const string& name, shared_ptr<Catalog> headCatalog);
	void DeleteFile(shared_ptr<File> file, shared_ptr<Catalog> headCatalog);
	void MoveFileToCatalog(shared_ptr<File> file, shared_ptr<Catalog> newCatalog, shared_ptr<Catalog> oldCatalog);
};

class File
{
public:
	File(const string& f_heading, const string& author, const time_t& cD);
protected:
	string heading;
	time_t creationDate;
	string author;
	const string getHeading();
	const string getAuthor();
	const time_t getCD();
	void setHeading(const string& head);
	friend class Secretary;
};

class Document : public File
{
	Document(const string& head, const string& author, const time_t& cD, const string& text);
private:
	string text;
	set<shared_ptr<Illustration>> illustrations;
protected:
	void UpdHeading(const string& head);
	void UpdText(const string& text);
	void LinkIllustration(shared_ptr<Illustration> ill);
	void UnlinkIllustration(shared_ptr<Illustration> ill);
	friend class Writer;
};

class Illustration : public File
{
	Illustration(const string& head, const string& author, const time_t& cD);
};

class Buffer
{
private:
	shared_ptr<Catalog> bufferCatalog;
	shared_ptr<Catalog> mainCatalog;
public:
	Buffer();
	shared_ptr<Catalog> getBuffer() const;
	shared_ptr<Catalog> getMain() const;
	void addFile(shared_ptr<File> file);
	friend class Illustrator;
};